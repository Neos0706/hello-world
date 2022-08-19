/*
    入口js
*/

import Vue from "vue";
import App from "./App";
import { Button } from "mint-ui"
import router from "./router";
import store from "./store"
import VueLazyload from "vue-lazyload";



import './mock/mockServer' //加载mockSever即可
import './fiters' // 全局过滤器
import loaderImg from './common/imgs/1.gif'


Vue.component(Button.name, Button) // <mt-button>
Vue.use(VueLazyload, {
    // 内部自定义一个指令lazy
    loading: loaderImg
})
Vue.config.productionTip = false

new Vue({
    el: "#app",
    render: h => h(App),
    router,
    store,

})