<template>
    <footer class="footer_guide border-1px">
        <div class="guide_item" @click="goTo('/msite')" :class="{on: '/msite'===$route.path}">
            <span class="item_icon">
                <i class="iconfont icon-food"></i>
            </span>
            <span>首页</span>
        </div>
        <div class="guide_item" @click="goTo('/search')" :class="{on: '/search'===$route.path}">
            <span class="item_icon">
                <i class="iconfont icon-search"></i>
            </span>
            <span>搜索</span>
        </div>
        <div class="guide_item" @click="goTo('/order')" :class="{on: '/order'===$route.path}">
            <span class="item_icon">
                <i class="iconfont icon-single"></i>
            </span>
            <span>订单</span>
        </div>
        <div class="guide_item" @click="goTo('/profile')" :class="{on: '/profile'===$route.path}">
            <span class="item_icon">
                <i class="iconfont icon-user"></i>
            </span>
            <span>我的</span>
        </div>
    </footer>
</template>

<script>
export default {
    name:'FooterGuide',
    methods:{
        goTo(path){
            this.$router.replace(path)
        }
    }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
/*引入公共样式*/
@import "../../common/stylus/mixins.styl"
.footer_guide
  // 顶部有白色的边框
  top-border-1px(#e4e4e4)
  position fixed
  z-index 100
  left 0
  right 0
  bottom 0
  background-color #fff
  width 100%
  height 50px
  display flex
  .guide_item
    display flex
    flex 1
    text-align center
    flex-direction column
    align-items center
    margin 5px
    color #999999
    &.on
      color limegreen
    span
      font-size 12px
      margin-top 2px
      margin-bottom 2px
      .iconfont
        font-size 22px
</style>