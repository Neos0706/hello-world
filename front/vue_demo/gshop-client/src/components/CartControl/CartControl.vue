<template>
    <div class="cartcontrol">
    <transition name="move">
      <div class="iconfont icon-removecircleoutline" v-if="food.count" @click.stop="updateFoodCount(false)"></div>
    </transition>
    <div class="cart-count" v-if="food.count">{{food.count}}</div>
    <div class="iconfont icon-addcircle" @click.stop="updateFoodCount(true)"></div>
  </div>
</template>

<script>
export default {
    name:'CartControl',
    props:['food'],
    methods:{
      updateFoodCount(isAdd){
        this.$store.dispatch('updateFoodCount',{isAdd,food:this.food})
      }
    }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../common/stylus/mixins.styl"
  .cartcontrol
    font-size: 0
    .cart-decrease
      display: inline-block
      padding: 6px
      line-height: 24px
      font-size: 24px
      color: limegreen

    .icon-removecircleoutline
      display: inline-block
      padding 6px
      line-height 24px
      font-size 24px
      color limegreen
      &.move-enter-active, &.move-leave-active
        transition all .3s
      &.move-enter, &.move-leave-to
        opacity 0
        transform translateX(15px) rotate(180deg)
    .cart-count
      display: inline-block
      vertical-align: top
      width: 12px
      padding-top: 6px
      line-height: 24px
      text-align: center
      font-size: 10px
      color: limegreen
    .icon-addcircle
      display: inline-block
      padding: 6px
      line-height: 24px
      font-size: 24px
      color limegreen
</style>
