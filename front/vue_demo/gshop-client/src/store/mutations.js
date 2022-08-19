// 直接更新state的多个方法的对象


import Vue from 'vue'
import {
    RECEIVE_ADDRESS,
    RECEIVE_CATEGORYS,
    RECEIVE_SHOPS,
    RECEIVE_USER_INFO,
    RESET_USER_INFO,
    RECEIVE_SHOP_GOODS,
    RECEIVE_SHOP_INFO,
    RECEIVE_SHOP_RATINGS,
    INCREMENT_GOOD_COUNT,
    DECREMENT_GOOD_COUNT,
    CLEAR_CART,
    RECEIVE_SEARCH_SHOPS
} from './mutation-types'

export default {
    [RECEIVE_ADDRESS](state, { address }) {
        state.address = address
    },
    [RECEIVE_CATEGORYS](state, { categorys }) {
        state.categorys = categorys
    },
    [RECEIVE_SHOPS](state, { shops }) {
        state.shops = shops
    },
    [RECEIVE_USER_INFO](state, { userInfo }) {
        state.userInfo = userInfo
    },
    // 退出登录，所以置为空对象
    [RESET_USER_INFO](state) {
        state.userInfo = {}
    },
    [RECEIVE_SHOP_GOODS](state, { shopGoods }) {
        state.shopGoods = shopGoods
    },
    [RECEIVE_SHOP_INFO](state, { shopInfo }) {
        state.shopInfo = shopInfo
    },
    [RECEIVE_SHOP_RATINGS](state, { shopRatings }) {
        state.shopRatings = shopRatings
    },
    [INCREMENT_GOOD_COUNT](state, { food }) {
        if (food.count) {
            food.count++
        } else {
            Vue.set(food, 'count', 1)
                //向购物车里加
            state.cartFoods.push(food)
        }
    },
    [DECREMENT_GOOD_COUNT](state, { food }) {
        if (food.count) {
            food.count--
                if (food.count === 0) {
                    // 从购物车里移除
                    state.cartFoods.splice(state.cartFoods.indexOf(food), 1)
                }
        }
    },
    //清空购物车
    [CLEAR_CART](state) {
        state.cartFoods.forEach(food => { food.count = 0 })
        state.cartFoods = []
    },

    [RECEIVE_SEARCH_SHOPS](state, { searchShops }) {
        state.searchShops = searchShops
    }

}