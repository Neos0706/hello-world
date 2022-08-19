function bindCaptchaBtnClick(){
    $('#captcha-btn').on("click",function (){
        let $this = $(this);
        let email = $("input[name='email']").val();
        if(email){
            //ajax 获取验证码
            $.ajax({
                url:"/user/captcha",
                method:"POST",
                data:{
                    email:email
                },
                success:function (res){
                    let code = res['code'];
                    if(code === 200){
                        //alert("验证码发送成功");
                        // 关闭点击事件
                        $this.off("click");
                        let countDown = 60;
                        // 开始倒计时
                        let timer = setInterval(function (){
                            countDown -= 1;
                            if(countDown > 0){
                                $this.text(countDown+"秒后重新发送");
                            }else{
                                $this.text("获取验证吗");
                                // 重新执行这个函数，重新绑定事件
                                bindCaptchaBtnClick();
                                // 清除定时器
                                clearInterval(timer);
                            }
                        }, 1000);
                    }else{
                        alert(res['message']);
                    }
                }
            })
        }else{
            alert("请输入邮箱")
            return;
        }

    })
}


$(function (){
    bindCaptchaBtnClick();
})