using System;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Text.RegularExpressions;

namespace macLookup
{
    internal class Program
    {
        
        private static readonly HttpClient Client = new HttpClient();
        
        public static void Main(string[] args)
        {

            if (args.Length != 1)
            {
                Console.WriteLine(
                    "Error: Not enough arguments provided.\nUsage: macLookup.exe [MAC address]\nMAC addresses can be " +
                    "in the format xx:xx:xx:xx:xx:xx or xx-xx-xx-xx-xx-xx");
                Environment.Exit(13);
            }

            var regex = new Regex(@"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$");

            var mac = args[0];

            if (!regex.IsMatch(mac))
            {
                Console.WriteLine("Error: That doesn't look like a valid MAC address");
            }
            
            var request = WebRequest.Create("https://api.macvendors.com/" + mac);

            var response = request.GetResponse();
            Console.WriteLine("Status response: " + ((HttpWebResponse)response).StatusDescription);

            string vendor;
            
            using (var dataStream = response.GetResponseStream())
            {
                var reader = new StreamReader(dataStream);
                vendor = reader.ReadToEnd();
            }

            response.Close();
            
            Console.WriteLine("Provided MAC: " + mac);
            Console.WriteLine("Vendor name: " + vendor);
            
        }
    }
}