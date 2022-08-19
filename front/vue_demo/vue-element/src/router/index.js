import Vue from "vue"
import Router from "vue-router"

Vue.use(Router)

// Layout 首页布局
import Layout from '@/layout';


export const constantRoutes = [{
        path: '',
        component: Layout,
        children: [{
            path: 'index',
            component: () =>
                import ('@/views/index'),
            name: 'Index',
        }]
    },
    {
        path: '/redirect',
        component: Layout,
    },
    {
        path: '/eldemo',
        component: Layout,
        children: [{
            path: '',
            component: () =>
                import ('@/views/Eldemo'),
            name: 'Eldemo'
        }]
    },
    {
        path: '/wayang',
        component: Layout,
        children: [{
            path: '',
            component: () =>
                import ('@/views/Wayang'),
            name: 'Wayang'
        }]
    },
]

export default new Router({
    mode: 'history',
    scrollBehavior: () => ({ y: 0 }),
    routes: constantRoutes
})