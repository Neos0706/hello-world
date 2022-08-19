// vue-router
import Vue from "vue";
import VueRouter from "vue-router"
// import Msite from "../pages/Msite/Msite"
// import Order from "../pages/Order/Order"
// import Profile from "../pages/Profile/Profile"
// import Search from "../pages/Search/Search"

// 路由组件懒加载
const Msite = () =>
    import ('../pages/Msite/Msite.vue')
const Search = () =>
    import ('../pages/Search/Search.vue')
const Order = () =>
    import ('../pages/Order/Order.vue')
const Profile = () =>
    import ('../pages/Profile/Profile.vue')

import Login from "../pages/Login/Login"
import Shop from "../pages/Shop/Shop"
import ShopGoods from "../pages/Shop/ShopGoods/ShopGoods"
import ShopRatings from "../pages/Shop/ShopRatings/ShopRatings"
import ShopInfo from "../pages/Shop/ShopInfo/ShopInfo"

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history', // 去掉地址中的哈希#
    routes: [{
            path: '/msite',
            component: Msite,
            // 此时的Msite等都是返回路由组件的函数，只有请求对应的路由路径时(第一次)才会执行此函数并加载路由组件
            // 标识此路由是否显示FooterGuide
            meta: {
                isShowFooter: true
            }
        }, {
            path: '/order',
            component: Order,
            meta: {
                isShowFooter: true
            }
        }, {
            path: '/profile',
            component: Profile,
            meta: {
                isShowFooter: true
            }
        },
        {
            path: '/search',
            component: Search,
            meta: {
                isShowFooter: true
            }
        }, {
            path: '/',
            redirect: '/msite'
        },
        {
            path: '/login',
            component: Login
        },
        {
            path: '/shop',
            component: Shop,
            children: [{
                    path: 'goods',
                    component: ShopGoods
                },
                {
                    path: 'info',
                    component: ShopInfo
                },
                {
                    path: 'ratings',
                    component: ShopRatings
                },
                {
                    path: '',
                    redirect: 'goods'
                }
            ]
        }
    ]
})