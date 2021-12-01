<template>
  <div class="register_con">
    <div class="l_con fl">
      <a class="reg_logo"><img src="@/assets/images/logo02.png"></a>
      <div class="reg_slogan">足不出户  ·  新鲜每一天</div>
      <div class="reg_banner"></div>
    </div>

    <div class="r_con fr">
      <div class="reg_title clearfix">
        <h1>用户注册</h1>
        <a href="login">登录</a>
      </div>
      <div class="reg_form clearfix">
        <form onsubmit="return verify()">
          <ul>
            <li>
              <label>用户名:</label>
              <input v-model="user.name" type="text" name="user_name" id="user_name" placeholder="5-20个字符" title="5-20个字符" required pattern="[\S]{5,20}">
              <span class="error_tip">提示信息</span>
            </li>
            <li>
              <label>密码:</label>
              <input v-model="user.password" type="password" name="pwd" id="pwd" required placeholder="8-20个字符" pattern="[\S]{8,20}">
              <span class="error_tip">提示信息</span>
            </li>
            <li class="reg_sub">
              <input type="submit" @click.prevent="register" value="注 册" name="">
            </li>
          </ul>
        </form>
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
    <p>CopyRight © 2016 北京天天生鲜信息技术有限公司 All Rights Reserved</p>
    <p>电话：010-****888    京ICP备*******8号</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "register",
  data(){
    return {
      user:{
        name:'',
        password:''
      }
    }
  },
  methods:{
    register(){
      axios.post('http://localhost:8000/user/register/',`username=${this.user.name}&password=${this.user.password}`).then(res=>{
        alert('注册成功!');
        this.$router.push('/');
      }).catch(err=>{
        alert('注册失败,请检查网络问题');
      })
    }
  }
}
</script>

<style scoped>

</style>