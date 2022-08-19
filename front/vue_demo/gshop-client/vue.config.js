const { defineConfig } = require('@vue/cli-service')
const NodePolyfillPlugin = require('node-polyfill-webpack-plugin')



module.exports = defineConfig({
    configureWebpack: config => {
        const plugins = []
        plugins.push(new NodePolyfillPlugin())
    },
    assetsDir: 'static',
    transpileDependencies: true,
    lintOnSave: false,
    // 代理配置表，在这里可以配置特定的请求代理到对应的API接口
    // 例如将'localhost:8080/api/xxx'代理到'www.example.com/api/xxx'
    devServer: {
        proxy: {
            'api': { //匹配所有以 '/api'开头的请求路径
                target: 'http://localhost:4001',
                // secure: false,  // 如果是https接口，需要配置这个参数
                changeOrigin: true, // 支持跨域
                pathRewrite: { // 重写路径: 去掉路径中开头的'/api'
                    '^/api': ''
                }
            }
        }
    }

})