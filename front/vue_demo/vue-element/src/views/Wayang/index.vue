<template>
    <div class="backgroud">
        <h1>wayang自动化测试job配置</h1>
        <div class="content">
            <!-- 设备状态 -->
            <DevInfo :devList="devList"></DevInfo>
            <div style="margin-top:20px"></div>
            <div class="pane-content">
                <el-tabs type="border-card">
                    <el-tab-pane label="设备配置">
                        <el-form label-width="80px" :model="form">
                            <el-card class="box-card">
                                <el-form-item label="上行设备">
                                    <el-select  multiple placeholder="Select" v-model="form.upDev" @blur="selectUpDev">
                                        <el-option
                                        v-for="dev in upDevList"
                                        :key="dev.name"
                                        :label="dev.name"
                                        :value="dev.name">
                                        </el-option>
                                    </el-select>
                                </el-form-item>
                            </el-card>
                            <el-card class="box-card">
                                <el-form-item label="下行设备">
                                    <el-select  multiple placeholder="Select" v-model="form.downDev" @blur="selectDownDev">
                                        <el-option
                                        v-for="dev in downDevList"
                                        :key="dev.name"
                                        :label="dev.name"
                                        :value="dev.name" >
                                        </el-option>
                                    </el-select>
                                </el-form-item>
                            </el-card>
                            <el-card class="box-card" v-show="form.downDev.length>=2">
                                <el-form-item label="弱网白名单">
                                    <el-select  multiple placeholder="Select" v-model="form.whiteList">
                                        <el-option
                                        v-for="(dev,index) in form.downDev"
                                        :key="index"
                                        :label="dev"
                                        :value="dev" >
                                        </el-option>
                                    </el-select>
                                </el-form-item>
                            </el-card>
                            <el-card class="box-card">
                                <el-form-item label="录屏设备">
                                    <el-select  multiple placeholder="Select" v-model="form.screenDev">
                                        <el-option
                                        v-for="dev in screenDev"
                                        :key="dev.name"
                                        :label="dev.name"
                                        :value="dev.name">
                                        </el-option>
                                    </el-select>
                                </el-form-item>
                            </el-card>
                        </el-form>
                        <el-button type="primary" @click="showForm">下一步</el-button>
                    </el-tab-pane>
                    <el-tab-pane label="用例配置">
                        <el-form label-width="100px"  label-position="left" :model="form">
                            <el-card class="box-card" style="padding-bottom:1em">
                                <el-col :span="24">
                                    <el-form-item label="私有参数" style="width: 80%">
                                        <el-input 
                                        type="textarea"
                                        autosize
                                        placeholder="多个私有参数使用英文逗号隔开"
                                        v-model="form.parameters">
                                        </el-input>
                                        <div><i class="el-icon-info">此处私有参数，勾选后同时设置上下行设备，若在设备配置中单独设置编码方式，此处会进行累加</i></div>                                   
                                    </el-form-item>
                                    <div>说明<el-tag>格式1</el-tag>{"rtc.log_size":200000}
                                            <el-tag>格式2</el-tag>{"wss://120-195-180-30.edge.agora.io:10000/":true}</div>
                                </el-col>
                            </el-card>
                            <el-card class="box-card" style="padding-bottom:1em">
                                <el-col :span="24">
                                    <el-form-item label="场景case组合" style="width: 100%">
                                        <el-row>
                                            <el-col :span="12">
                                                <el-select  multiple placeholder="请选择场景组合" v-model="form.selectCaseTypeList">
                                                    <el-option
                                                    v-for="caseType in caseList"
                                                    :key="caseType.name"
                                                    :label="caseType.name"
                                                    :value="caseType.name" >
                                                    </el-option>
                                                </el-select>
                                            </el-col>
                                            <el-col :span="12">
                                                <i class="el-icon-info">场景case仅适用于1v1,场景包含上下行role以及video_source, 勾选case会覆盖第一页所填写的配置</i>
                                            </el-col>
                                        </el-row>                          
                                    </el-form-item>
                                    <el-form-item label="场景case号" style="width: 100%">
                                        <el-input 
                                        type="textarea"
                                        autosize
                                        placeholder="多个case请用空格隔开"
                                        v-model="form.selectCaseType">
                                        </el-input>
                                            
                                    </el-form-item>                                    
                                </el-col>
                            </el-card> 
                            <el-card class="box-card" style="padding-bottom:1em">
                                <el-col :span="24">
                                    <el-form-item label="弱网case组合" style="width: 100%">
                                        <el-row>
                                            <el-col :span="12">
                                                <el-select  multiple placeholder="请选择弱网组合" v-model="form.CaseList">
                                                    <el-option
                                                    v-for="caseType in liveCaseList"
                                                    :key="caseType.name"
                                                    :label="caseType.name"
                                                    :value="caseType.name" >
                                                    </el-option>
                                                </el-select>
                                            </el-col>
                                        </el-row>                          
                                    </el-form-item>
                                    <el-form-item label="场景case号" >
                                        <el-input 
                                        type="textarea"
                                        autosize
                                        placeholder="多个case请用空格隔开"
                                        v-model="form.selectCase">
                                        </el-input>
                                            
                                    </el-form-item>                                    
                                </el-col>
                            </el-card>
                            <el-card class="box-card" style="padding-bottom:1em">
                                    <el-form-item label="视频参数" >
                                        <el-input 
                                        v-model="form.videoProfile">
                                        </el-input>                                            
                                    </el-form-item>
                                    <el-form-item label="编码方式" >
                                        <el-row>
                                            <el-col :span="6">
                                                <el-radio v-model="form.codeRadio" label="1">h264</el-radio>
                                                <el-radio v-model="form.codeRadio" label="2">vp8</el-radio>
                                            </el-col>
                                            <el-col :span="18">
                                                <i class="el-icon-info">此处编码方式优先级最低，勾选后同时设置上下行设备，若在设备配置中单独设置编码方式，会将此处设置覆盖</i>
                                            </el-col>
                                        </el-row>                                            
                                    </el-form-item>
                                    <el-form-item label="重跑次数" >
                                        <el-input-number v-model="form.repeatNum" :min="1" :max="10"></el-input-number>                                       
                                    </el-form-item>  
                            </el-card>
                            <el-card class="box-card">
                                <el-collapse>
                                    <el-collapse-item title="选填项 (测试版本备注、描述备注、appid更改)" name="1">
                                        <el-form-item label="测试版本" >
                                            <el-input 
                                            v-model="form.sdkNum" placeholder="选填">
                                            </el-input>                                            
                                        </el-form-item>
                                        <el-form-item label="测试描述" >
                                            <el-input 
                                            v-model="form.sdkDescription" placeholder="选填">
                                            </el-input>                                            
                                        </el-form-item>
                                        <el-form-item label="appid" >
                                            <el-input 
                                            v-model="form.appid">
                                            </el-input>                                            
                                        </el-form-item>
                                    </el-collapse-item>
                                </el-collapse>
                            </el-card>
                        </el-form>
                        <el-button type="primary">上一步</el-button>
                        <el-button type="primary">下一步</el-button>
                    </el-tab-pane>
                    <el-tab-pane label="测评配置">
                        <el-form label-width="100px"  label-position="left" :model="form">
                        <el-form-item label="即时配送">
                            <el-switch
                                v-model="form.isScreen"
                                active-color="#13ce66"
                                inactive-color="#ff4949">
                            </el-switch>
                        </el-form-item>                                            
                        <el-form-item label="录屏时长" >
                             <el-slider
                                v-model="form.screenTime"
                                show-input :max="360">
                                </el-slider>  
                        </el-form-item>
                        <el-form-item label="计算主观卡顿率" >
                            <el-switch
                                v-model="form.isFreezeRate"
                                active-color="#13ce66"
                                inactive-color="#ff4949">
                            </el-switch>
                            <div v-if="form.isFreezeRate"><i class="el-icon-info">建议使用yuv源，若选择camera请确保地球仪工作正常且在设备采集画面内</i></div>                                             
                        </el-form-item>
                        <el-form-item label="计算主观延时" >
                            <el-switch
                                v-model="form.isDelay"
                                active-color="#13ce66"
                                inactive-color="#ff4949">
                            </el-switch>
                            <div v-if="form.isDelay"><i class="el-icon-info">请确定上行设备使用camera，并且面对NTP对时源</i></div>                                            
                        </el-form-item>
                        <el-form-item label="计算主观画质" >
                            <el-switch
                                v-model="form.isVQA"
                                active-color="#13ce66"
                                inactive-color="#ff4949">
                            </el-switch>
                            <div v-if="form.isVQA"><i class="el-icon-info">计算VQA较慢</i></div>                                            
                        </el-form-item>
                        <el-form-item label="计算客观指标" >
                            <el-switch
                                v-model="form.isCalLog"
                                active-color="#13ce66"
                                inactive-color="#ff4949">
                            </el-switch>
                            <div v-if="form.isCalLog"><i class="el-icon-info">仅支持计算native/arsenal wayang （web wayang无本地log）</i></div>                                            
                            </el-form-item>
                        </el-form>
                        <el-button type="primary">上一步</el-button>
                        <el-button type="primary">下一步</el-button>
                    </el-tab-pane>
                    <el-tab-pane label="常规配置 & 提交">
                        <el-form label-width="100px"  label-position="left" :model="form">
                            <el-button @click="addEmail">新增邮箱</el-button>
                            <!-- <el-form-item label="邮箱0" >
                                <el-input placeholder="请输入内容" v-model="form.email[0]">
                                    <template slot="append">@agora.io</template>
                                </el-input>
                                <el-button @click="deleteEmail">删除</el-button>
                            </el-form-item> -->
                            <Email v-for="(obj,index) in form.emailList" :key="index" :index="index" :emailObj="obj" :deleteEmail="deleteEmail"></Email>   
                            <el-form-item label="弱网机参数" >
                            <el-form-item  label="ip" style="width:300px; margin-left: 120px;"><el-input v-model="form.ip" placeholder="请输入ip"  size="small"></el-input> </el-form-item>
                            <el-form-item  label="端口" style="width:300px; margin-left: 120px"><el-input v-model="form.port" placeholder="请输入端口"  size="small"></el-input> </el-form-item>
                            <el-form-item  label="用户名" style="width:300px; margin-left: 120px"><el-input v-model="form.username" placeholder="请输入用户名"  size="small"></el-input> </el-form-item>
                            <el-form-item  label="密码" style="width:300px; margin-left: 120px"><el-input v-model="form.password" placeholder="请输入密码"  size="small"></el-input> </el-form-item>
                                                                            
                            </el-form-item>
                        </el-form>
                        <el-button type="primary">上一步</el-button>
                        <el-button type="primary">开始构建(通过jenkins)</el-button>
                        <el-button type="primary">开始构建</el-button>
                    </el-tab-pane>
                    <el-tab-pane label="主控机">主控机
                        <OneDevSetting :form="form"></OneDevSetting>                       
                    </el-tab-pane>
                </el-tabs>
            </div>
        </div>
    </div>
</template>

<script>
import Email from '@/components/Email';
import DevInfo from '@/components/DevInfo';
import OneDevSetting from '@/components/OneDevSetting'
export default {
    name:'Wayang',
    data(){
        var validatePass = ()=>{

        }
        return  {
            // on:是否被占用,默认fasle devChioce: 
            // devChioce: 0 没用被选中  1 被上行选中 2被下行选中
            devList:[{name:'android_MI8',on:false,devChioce:0}, 
            {name:'ios_iphone8_plus',on:false,devChioce:0},
            {name:'ios_iphoneX_lab', on:false, devChioce:0},
            {name:'mac_air', on:false, devChioce:0},
            {name:'mac_pro',on:false, devChioce:0},
            {name:'win_thinkpad', on:false, devChioce:0},
            {name:'win_xiaomi',on:false, devChioce:0}],
            // 场景case组合
            caseList:[
                {name:'Basic', caseArr:[500,533,667,675,209,233]},
                {name:'FirstDraw',caseArr:[505,533,511,512,513,514,515]},
                {name:'NoLoss', caseArr:[200,204,216,220,629,630,671,674]},
                {name:'NetImpair', caseArr:[201,202,203,207,208,209,210,211,217,218,219,223,224,225,226,227,242]},
                {name:'NetBoundary', caseArr:[243,244,245,246,247,248,249,250,251,252,253]}

            ],
            //弱网case组合
            liveCaseList:[
                {name:'liveCases',caseArr:['no','up_loss_50','up_rate_500_loss_10','down_loss_30','down_delay_200_jitter_300','down_delay_100_jitter_200','down_rate_500_loss_10']},
                {name:'commCases', caseArr:['up_loss_30','up_rate_500_loss_20','up_delay_100_jitter_300','down_loss_30']}
            ],
            // 
            form:{
                // 第一页表单
                // 上行设备
                upDev:[],
                // 下行设备
                downDev:[],
                // 弱网白名单, 下行弱网大于2才会有
                whiteList:[],
                screenDev:[],

                // 第二页表单
                // 设置的私有参数
                parameters:'',
                // 选择的场景case  组合
                selectCaseTypeList:[],
                // case号
                selectCaseType:'',
                // 选择的弱网case 组合
                selectCaseList:[],
                // case号
                selectCase:'',
                // 视频profile
                videoProfile:'640*480*15*500',
                // codeRadio 1:h264, 2:vp8
                codeRadio:'1',
                // 重跑次数
                repeatNum:1,
                // 测试版本
                sdkNum:'',
                // 测试描述
                sdkDescription:'',
                // appid
                appid:'aab8b8f5a8cd4469a63042fcfafe7063',

                //  第三页表单
                //是否屏幕录制
                isScreen:true,
                //录屏时长
                screenTime:180,
                //是否计算主观卡顿率
                isFreezeRate:false,
                //是否计算主观延时
                isDelay:false,
                //是否计算主观画质
                isVQA:false,
                //是否计算客观指标
                isCalLog:true,

                // 第四页表单
                // 邮箱 列表 这里设置邮箱为对象 是为了防止子组件修改父组件数据报错(对象可以其他不行)
                emailList:[{
                    email:'lumeng'
                },{
                    email:'guoqi'
                }],
                // 弱网机ip
                ip:'10.96.0.73',
                // 弱网机端口
                port:'22',
                // 弱网机用户名
                username:'agora',
                // 弱网机密码
                password:'bestvoip',
            },


        }
    },
    components:{Email,DevInfo,OneDevSetting},
    computed:{
        // 空闲机器
        devFreeList(){
            return this.devList.filter(item=>{return !item.on})
        },
        upDevList(){
            return this.devFreeList.filter(item=>{return item.devChioce==0})
        },
        downDevList(){
            return this.devFreeList.filter(item=>{return item.devChioce==0})
        },
        //屏幕录制机器
        screenDev(){
            return this.devFreeList.filter(item=>{ return item.devChioce==1 || item.devChioce==2})
        }
    },
    methods:{
        showForm(){
            console.log(this.form)
        },
        // 上行设备选中后执行的回调
        selectUpDev(e){
            this.devFreeList.forEach(item => {
                if (this.form.upDev.includes(item.name)){
                    item.devChioce = 1
                }           
            });
        },
        // 下行行设备选中后执行的回调
        selectDownDev(e){
            console.log(this.form.downDev)
            this.devFreeList.forEach(item => {
                if (this.form.downDev.includes(item.name)){
                    item.devChioce = 2
                }                
            })
            console.log("downDevList", this.downDevList)
        },
        // 关于邮箱组件的操作
        addEmail(e){
            this.form.emailList.push({email:''})
        },
        // 需要传递给子组件
        deleteEmail(index){
            this.form.emailList.splice(index,1)
        },

    }

}
</script>

<style lang="css" scoped>
.backgroud{
    width: 100%;
    height:100%;
    background: url(/src/assets/images/backgroud.jpg);
    background-size: 100% 100%;
    position: sticky;
}
.content{
    text-align: center;
    background-color: rgba(110, 111, 109, 0.819);
    margin-left: 5%;
    margin-right: 5%;
}
</style>