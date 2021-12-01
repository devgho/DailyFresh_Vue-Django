<template>
  <div class="login_top clearfix">
    <a href="/" class="login_logo"><img src="@/assets/images/logo02.png"></a>
  </div>
  <div id="feng">
    <div class="login_form_bg">
      <div class="login_form_wrap clearfix">
        <div class="login_banner fl"></div>
        <div class="slogan fl">日夜兼程 · 急速送达</div>
        <div class="login_form fr">
          <div class="login_title clearfix">
            <h1>用户登录</h1>
            <a href="register">立即注册</a>
          </div>
          <div class="form_input">
            <form action="/" method="GET" @submit.prevent="verify()">
              <input type="text" id="uname" name="username" v-model="uname" required class="name_input" placeholder="请输入用户名">
              <div class="user_error">输入错误</div>
              <input type="password" id="pwd" name="pwd" v-model="pwd" required class="pass_input" placeholder="请输入密码">
              <div class="pwd_error">输入错误</div>
              <div class="more_input clearfix">
                <input type="checkbox" name="">
                <label>记住用户名</label>
                <a href="#">忘记密码</a>
              </div>
              <input type="submit" name="" value="登录" class="input_submit">
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="footer no-mp">
    <div class="foot_link">
      <a href="#">关于我们</a>
      <span>|</span>
      <a href="#">联系我们</a>
      <span>|</span>
      <a href="#">招聘人才</a>
      <span>|</span>
      <a href="#">友情链接</a>
    </div>
    <p>CopyRight © 2016 北京某某信息技术有限公司 All Rights Reserved</p>
    <p>电话：010-****888    京ICP备*******8号</p>
  </div>
</template>

<script>
import axios from "axios";
import {ref} from "vue";
import {useStore} from 'vuex'
import router from "@/router";

// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
// axios.defaults.transformRequest = [function (data) {
//   let ret = ''
//   for (let it in data) {
//     ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
//   }
//   return ret
// }]

export default {
  name: "Login",
  setup(){
    const store = useStore();
    let uname = ref();
    let pwd = ref();
    function verify(){
      axios.post('http://localhost:8000/user/login/',`username=${uname.value}&password=${pwd.value}`).then(res=>{
        if (res.data.message=='true'){
          alert('登录成功');
          store.commit('login',res.data.user);
          router.push('/');
        }else{
          alert('登录失败'+res.data.message);
        }
      }).catch(err=>{
        alert('错误'+err);
      })
      return false;
    }
    return {
      uname,
      pwd,
      verify
    }
  }
}
</script>

<style scoped>

</style>