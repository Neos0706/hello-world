<template>
    <section class="loginContainer">
    <div class="loginInner">
      <div class="login_header">
        <h2 class="login_logo">外卖</h2>
        <div class="login_header_title">
          <a href="javascript:;" :class="{on: loginWay}" @click="loginWay=true">短信登录</a>
          <a href="javascript:;" :class="{on: !loginWay}" @click="loginWay=false" >密码登录</a>
        </div>
      </div>
      <div class="login_content">
        <form @submit.prevent="login">
          <!-- 短信登陆 -->
          <div :class="{on: loginWay}">
            <section class="login_message">
              <input type="tel" maxlength="11" placeholder="手机号" v-model="phone">
              <button  :disabled="!rightPhone" class="get_verification" :class="{right_phone:rightPhone}" @click.prevent="getCode">{{codeTime?`已发送${codeTime}s`:'发送验证码'}}</button>
            </section>
            <section class="login_verification">
              <input type="tel" maxlength="8" placeholder="验证码" v-model="code">
            </section>
            <section class="login_hint">
              温馨提示：未注册外卖帐号的手机号，登录时将自动注册，且代表已同意
              <a href="javascript:;">《用户服务协议》</a>
            </section>
          </div>
          <!-- 密码登陆 -->
          <div  :class="{on: !loginWay}">
            <section>
              <section class="login_message">
                <input type="text" maxlength="11" placeholder="手机/邮箱/用户名" v-model="name">
              </section>
              <section class="login_verification">
                <!-- 是否显示密码 -->
                <input type="text" maxlength="8" placeholder="密码" v-model="pwd" v-if="showPwd">
                <input type="password" maxlength="8" placeholder="密码" v-model="pwd" v-else>
                <div class="switch_button off" :class="showPwd?'on':'off'" @click="showPwd=!showPwd">
                  <div class="switch_circle" :class="{right:showPwd}"></div>
                  <span class="switch_text">{{showPwd?'':''}}</span>
                </div>
              </section>
              <section class="login_message">
                <input type="text" maxlength="11" placeholder="验证码" v-model="captcha" >
                <img class="get_verification" src="http://localhost:4001/captcha" alt="captcha" ref="captcha" @click="getCaptcha">
              </section>
            </section>
          </div>
          <button class="login_submit">登录</button>
        </form>
        <a href="javascript:;" class="about_us">关于我们</a>
      </div>
      <!--利用$router.back()返回上一级路由 -->
      <a href="javascript:" class="go_back" @click="$router.back()">
        <i class="iconfont icon-arrow-left"></i>
      </a>
    </div>
    <!-- 提示组件,closeTip事件在其中被分发出来 -->
    <AlertTip :alertText="alertText" v-show="alertShow" @closeTip="closeTip" />
  </section>
</template>

<script>
import AlertTip from '@/components/AlertTip/AlertTip.vue'
import {reqPwdLogin,reqSendCode,reqSmsLogin} from '@/api/index'
export default {
    name:'Login',
    data() {
      return {

        // 短信登录
        loginWay:true,// true 代表短信登录，false代表手机登录
        phone:'', //手机号
        codeTime:0, //验证码倒计时值
        showPwd:false, //是否显示密码 默认不显示
        code:'', //手机验证码
        // 密码登录
        name:'', //用户名
        pwd:'',  // 用户密码
        captcha:'', // 验证码
        alertText:'', //提示文本
        alertShow: false // 是否显示提示框
      }
    },
    components:{
      AlertTip
    },
    computed:{
      rightPhone(){
        return /^1[3-9]\d{9}$/.test(this.phone)
      }
    },
    methods:{
      // 获取短信验证吗
      async getCode(){
        if(!this.codeTime){
          this.codeTime = 30
          this.intervalID = setInterval(() => {
            this.codeTime--
            if(this.codeTime <= 0){
              clearInterval(this.intervalID)
            }            
          }, 1000);
        }
        const result = await reqSendCode(this.phone)
        if (result.code==1){
          // 需要花钱买服务，暂时弹出验证码
          this.showAlert(result.msg)
          if(this.codeTime){
            clearInterval(this.intervalID)
            this.codeTime = 0
          }
        }
      },
      // 获取图片验证码
      getCaptcha(){
        this.$refs.captcha.src="http://localhost:4001/captcha?time=" + Date.now()
      },
      // 控制显示提示框
      showAlert(alertText){
        this.alertShow = true
        this.alertText = alertText
      },
      // 关闭提示框
      closeTip(){
        this.alertShow = false
        this.alertText =''
      },
      async login(){
          let result
        // 判断是短信登录还是用户密码登录
        if(this.loginWay){//短信登录
          const {phone,code,rightPhone} = this
          if(!rightPhone){
            this.showAlert('手机号不正确')
            return
          }else if(!/^\d{6}$/.test(code)){
            this.showAlert('验证码必须是6位数字')
            return
          }
          // 发送ajax短信登录请求
          result = await reqSmsLogin(phone,code)
        }else{
          const {name,pwd,captcha} = this
          if(!name) {
            this.showAlert('请输入用户名')
            return
          }else if(!pwd){
            this.showAlert('密码不能为空')
            return
          }else if(!captcha){
            this.showAlert('验证码不能为空')
            return
          }
          result = await reqPwdLogin(name,pwd,captcha)
        }
        if(result.code==0){
          // 给user复制
          const userInfo = result.data
          this.$store.dispatch('recordUesr',userInfo)
          this.$router.replace('/profile')
        }else{
          this.showAlert(result.msg)
          this.getCaptcha()
        }

      }
    }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../common/stylus/mixins.styl"
  .loginContainer
    width 100%
    height 100%
    background #fff
    .loginInner
      padding-top 60px
      width 80%
      margin 0 auto
      .login_header
        .login_logo
          font-size 40px
          font-weight bold
          color limegreen
          text-align center
        .login_header_title
          padding-top 40px
          text-align center
          >a
            color #333
            font-size 14px
            padding-bottom 4px
            &:first-child
              margin-right 40px
            &.on
              color limegreen
              font-weight 700
              border-bottom 2px solid limegreen
      .login_content
        >form
          >div
            display none
            &.on
              display block
            input
              width 100%
              height 100%
              padding-left 10px
              box-sizing border-box
              border 1px solid #ddd
              border-radius 4px
              outline 0
              font 400 14px Arial
              &:focus
                border 1px solid limegreen
            .login_message
              position relative
              margin-top 16px
              height 48px
              font-size 14px
              background #fff
              .get_verification
                position absolute
                top 50%
                right 10px
                transform translateY(-50%)
                border 0
                color #ccc
                font-size 14px
                background transparent
                &.right_phone
                  color black
            .login_verification
              position relative
              margin-top 16px
              height 48px
              font-size 14px
              background #fff
              .switch_button
                font-size 12px
                border 1px solid #ddd
                border-radius 8px
                transition background-color .3s,border-color .3s
                padding 0 6px
                width 30px
                height 16px
                line-height 16px
                color #fff
                position absolute
                top 50%
                right 10px
                transform translateY(-50%)
                &.off
                  background #fff
                  .switch_text
                    float right
                    color #ddd
                &.on
                  background limegreen
                >.switch_circle
                  //transform translateX(27px)
                  position absolute
                  top -1px
                  left -1px
                  width 16px
                  height 16px
                  border 1px solid #ddd
                  border-radius 50%
                  background #fff
                  box-shadow 0 2px 4px 0 rgba(0,0,0,.1)
                  transition transform .3s
                  &.right
                    transform translateX(30px)
            .login_hint
              margin-top 12px
              color #999
              font-size 14px
              line-height 20px
              >a
                color limegreen
          .login_submit
            display block
            width 100%
            height 42px
            margin-top 30px
            border-radius 4px
            background #4cd96f
            color #fff
            text-align center
            font-size 16px
            line-height 42px
            border 0
        .about_us
          display block
          font-size 12px
          margin-top 20px
          text-align center
          color #999
      .go_back
        position absolute
        top 5px
        left 5px
        width 30px
        height 30px
        >.iconfont
          font-size 20px
          color #999
</style>
