// 包含基于state的getter计算属性的对象

export default {
    totalCount(state) {
        return state.cartFoods.reduce((total, food) => total + food.count, 0)
    },
    totalPrice(state) {
        return state.cartFoods.reduce((total, food) => total + food.count * food.price, 0)
    },
    positiveSize(state) {
        return state.shopRatings.reduce((total, rating) => total + (rating.text.length > 0 ? 1 : 0), 0)
    }
}