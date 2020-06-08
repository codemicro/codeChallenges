using System;
using System.ComponentModel;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Windows.Controls;
using System.Windows.Media.Imaging;
using System.Windows.Threading;

namespace imageNoise
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow
    {
        private readonly BackgroundWorker worker = new BackgroundWorker();
        private readonly DispatcherTimer Timer = new DispatcherTimer();
        
        private const int ImageWidth = 320;
        private const int ImageHeight = 240;
        private readonly Random _randomGenerator = new Random();

        private DateTime FpsTimer = DateTime.Now;

        public MainWindow()
        {
            InitializeComponent();

            worker.DoWork += delegate
            {
                Dispatcher.BeginInvoke((Action) (() => { noiseImageViewer.Source = GenerateNoiseImage(); }));
            };
            worker.RunWorkerCompleted += UpdateFps;

            void OnTick(object sender, object e)
            {
                try
                {
                    worker.RunWorkerAsync();
                } catch (InvalidOperationException) { }  // previous tick has not finished
            }
           
            Timer.Interval = TimeSpan.FromMilliseconds(16);  // 60fps maximum
            Timer.Tick += OnTick;

            Timer.Start();
        }

        private BitmapImage GenerateNoiseImage()
        {
            var generatedImage = new Bitmap(ImageWidth, ImageHeight);
            var convertedImage = new BitmapImage();
            
            for (var x = 0; x < generatedImage.Width; x++)
            {
                for (var y = 0; y < generatedImage.Height; y++)
                {
                    var color = _randomGenerator.Next(2) == 0 ? Color.Black : Color.White;
                    generatedImage.SetPixel(x, y, color);
                }
            }

            using (var memory = new MemoryStream())
            {
                generatedImage.Save(memory, ImageFormat.Bmp);
                memory.Position = 0;
                
                convertedImage.BeginInit();
                convertedImage.StreamSource = memory;
                convertedImage.CacheOption = BitmapCacheOption.OnLoad;
                convertedImage.EndInit();
            }
            
            return convertedImage;
            
        }

        private void UpdateFps(object sender, RunWorkerCompletedEventArgs e)
        {
            var now = DateTime.Now;
            var fps = Math.Round(1 / (now - FpsTimer).TotalSeconds, 0);
            FpsTimer = now;

            Dispatcher.BeginInvoke((Action) (() => { fpsIndicator.Text = fps.ToString(); }));
        }
        
    }
}