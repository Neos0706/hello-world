// Action 通过mutation间接更新state的多个方法对象，这里写一些业务逻辑

import {
    RECEIVE_ADDRESS,
    RECEIVE_CATEGORYS,
    RECEIVE_SHOPS,
    RECEIVE_USER_INFO,
    RESET_USER_INFO,
    RECEIVE_SHOP_GOODS,
    RECEIVE_SHOP_RATINGS,
    RECEIVE_SHOP_INFO,
    INCREMENT_GOOD_COUNT,
    DECREMENT_GOOD_COUNT,
    CLEAR_CART,
    RECEIVE_SEARCH_SHOPS

} from './mutation-types'

import {
    reqAddress,
    reqCategorys,
    reqShops,
    reqUserInfo,
    reqLogout,
    reqShopGoods,
    reqShopRatings,
    reqShopInfo,
    reqSearchShop
} from "../api/index"

export default {
    // 异步获取地址
    async getAddress(content) {
        const geohash = content.state.latitude + ',' + content.state.longitude
        const result = await reqAddress(geohash)
        if (result.code === 0) {
            const address = result.data
            content.commit(RECEIVE_ADDRESS, { address })
        }
    },
    // 获取食品分类
    async getCategorys(content) {
        const result = await reqCategorys()
        if (result.code === 0) {
            const categorys = result.data
            content.commit(RECEIVE_CATEGORYS, { categorys })
        }
    },
    //获取商家列表
    async getShops(content) {
        const { latitude, longitude } = content.state
        const result = await reqShops({ latitude, longitude })

        if (result.code === 0) {
            const shops = result.data
            content.commit(RECEIVE_SHOPS, { shops })
        }
    },
    //同步记录用户信息，随登录已经从服务器传回来了
    recordUesr(content, userInfo) {
        content.commit(RECEIVE_USER_INFO, { userInfo })
    },
    // 异步请求用户信息，服务器内有持久化session
    async getUserInfo({ commit }) {
        const result = await reqUserInfo()
        if (result.code === 0) {
            const userInfo = result.data
            commit(RECEIVE_USER_INFO, { userInfo })
        }
    },
    //异步退出登录
    async logout({ commit }) {
        const result = await reqLogout()
        if (result.code === 0) {
            commit(RESET_USER_INFO)
        }
    },
    // 异步获取商家货品 其实是被mock拦截
    async getShopGoods({ commit }, callback) {
        const result = await reqShopGoods()
        if (result.code === 0) {
            const shopGoods = result.data
            commit(RECEIVE_SHOP_GOODS, { shopGoods })
            callback && callback()
        }
    },
    // 异步获取商家评论 其实是被mock拦截
    async getShopRatings({ commit }, callback) {
        const result = await reqShopRatings()
        if (result.code === 0) {
            const shopRatings = result.data
            commit(RECEIVE_SHOP_RATINGS, { shopRatings })
            callback && callback()
        }
    },
    // 异步获取商家信息 其实是被mock拦截
    async getShopInfo({ commit }) {
        const result = await reqShopInfo()
        if (result.code === 0) {
            const shopInfo = result.data
            commit(RECEIVE_SHOP_INFO, { shopInfo })
        }
    },
    //本地同步更新商品购物量
    updateFoodCount({ commit }, { isAdd, food }) {
        if (isAdd) {
            commit(INCREMENT_GOOD_COUNT, { food })
        } else {
            commit(DECREMENT_GOOD_COUNT, { food })
        }
    },
    clearCart({ commit }) {
        commit(CLEAR_CART)
    },
    async getSearchShops({ commit, state }, keyword) {
        const geohash = state.latitude + ',' + state.longitude
        const result = await reqSearchShop(geohash, keyword)
        if (result.code === 0) {
            const searchShops = result.data
            commit(RECEIVE_SEARCH_SHOPS, { searchShops })
        }
    }

}