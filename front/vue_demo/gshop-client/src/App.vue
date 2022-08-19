<template>
    <div>
        <router-view/>
        <FooterGuide v-show="$route.meta.isShowFooter"/>
    </div>
</template>
<script>
import {mapActions} from 'vuex'
import FooterGuide from './components/FooterGuide/FooterGuide.vue'

export default {
    name:'app',
    components:{
        FooterGuide
    },
    //  声明一个异步函数
    mounted(){
        this.getAddress()
        this.getUserInfo()
    },
    methods:{
        ...mapActions(['getAddress','getUserInfo'])
    }
}
</script>

<style  lang="stylus" rel="stylesheet/stylus">
    .app
        color: read
</style>>

