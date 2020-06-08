using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Windows.Media.Imaging;

namespace imageNoise
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow
    {
        private const int ImageWidth = 320;
        private const int ImageHeight = 240;
        private readonly Random RandomGenerator = new Random();
        
        public MainWindow()
        {
            InitializeComponent();

            noiseImageViewer.Source = GenerateNoiseImage();

        }

        private BitmapImage GenerateNoiseImage()
        {
            var generatedImage = new Bitmap(ImageWidth, ImageHeight);
            var convertedImage = new BitmapImage();
            
            for (var x = 0; x < generatedImage.Width; x++)
            {
                for (var y = 0; y < generatedImage.Height; y++)
                {
                    var color = RandomGenerator.Next(2) == 0 ? Color.Black : Color.White;
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
    }
}