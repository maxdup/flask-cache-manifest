var path = require('path');
const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');

var srcdir = './src_bundle2';
var distdir = './bundle2';

bundle = {
  entry: {
    app: path.resolve(srcdir, 'app.js'),
  },
  output: {
    path: path.resolve(__dirname, distdir),
  }
}

module.exports = merge(common, bundle)
