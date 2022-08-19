<template>
    <section class="app-main">
        <transition name="fade-transform" mode="out-in">
        <keep-alive >
            <router-view :key="key"/>
        </keep-alive>
        </transition>
    </section>
  
</template>

<script>
export default {
    name: 'AppMain',
    computed:{
        key(){
            //console.log(`this.$route.path===>${this.$route.path}`)
            return this.$route.path
        }
    }
}
</script>

<style lang="scss" scoped>
.app-main {
  /* 50= navbar  50  */
  min-height: calc(100vh - 50px);
  width: 100%;
  position: relative;
  overflow: hidden;
}

</style>