const webpack = require('webpack')
const DotEnv = require('dotenv')

dotEnv = new webpack.DefinePlugin({
    "process.env": {
    'API_BASE_URL': JSON.stringify(process.env.API_BASE_URL),
   }
})

module.exports = {
    configureWebpack: {
      plugins: [
        dotEnv
      ]
    }
  }