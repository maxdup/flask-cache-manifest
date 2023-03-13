var webpack = require('webpack');
var path = require('path');

var srcdir1 = './src_bundle1';
var srcdir2 = './src_bundle2';
var srcdir3 = './src_bundle3';

const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const filenames = "[name].[contenthash].css";

const { WebpackManifestPlugin } = require('webpack-manifest-plugin');

config = {
  mode: 'production',
  output: {
    publicPath: '', // This is important, Webpack 5 defaults to 'auto'
    filename: "[name]-[contenthash].js",
    clean: true
  },
  plugins: [
    new MiniCssExtractPlugin({ filename: filenames }),
    new WebpackManifestPlugin({
      fileName: "cache_manifest.json"
    }),
  ],

  module: {
    rules: [
      { test: /\.css$/,
        use: [
          { loader: MiniCssExtractPlugin.loader },
          { loader: 'css-loader' },
        ]
      }
    ]
  },
}

module.exports = config;
