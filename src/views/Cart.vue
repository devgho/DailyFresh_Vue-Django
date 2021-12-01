<template>
  <div id="tt">
    <div class="header_con">
      <div class="header">
        <div class="welcome fl">欢迎来到天天生鲜!</div>
        <div class="fr">
          <div class="login_info fl">
            欢迎您：<em>刘 博</em>
          </div>
          <div class="login_btn fl" v-if="this.$store.state.user==''">
            <a href="login">登录</a>
            <span>|</span>
            <a href="register">注册</a>
          </div>
          <div class="user_link fl" v-else>
            <span>|</span>
            <a href="user_center_info">用户中心</a>
            <span>|</span>
            <a href="cart">我的购物车</a>
            <span>|</span>
            <a href="user_center_info">我的订单</a>
          </div>
        </div>
      </div>
    </div>
    <div class="search_bar clearfix">
      <a href="/" class="logo fl"><img src="@/assets/images/logo.png"></a>
      <div class="sub_page_name fl">|&nbsp;&nbsp;&nbsp;&nbsp;购物车</div>
    </div>
    <div class="total_count">全部商品<em>4</em>件</div>
    <ul class="cart_list_th clearfix">
      <li class="col01">商品名称</li>
      <li class="col02">商品单位</li>
      <li class="col03">商品价格</li>
      <li class="col04">数量</li>
      <li class="col05">小计</li>
      <li class="col06">操作</li>
    </ul>
    <ul class="cart_list_td clearfix" v-for="good in goods" :key="good.id">
      <li class="col01"><input type="checkbox" v-model="checkModel" :value="good.id"></li>
      <li class="col02"><img :src="good.image"></li>
      <li class="col03">{{good.name}}<br><em>{{good.price}}元/500g</em></li>
      <li class="col04">500g</li>
      <li class="col05">{{good.price}}</li>
      <li class="col06">
        <div class="num_add">
          <a href="javascript:;" @click.prevent="good.sl++" class="add fl">+</a>
          <input type="text" class="num_show fl" v-model="good.sl">
          <a href="javascript:;" @click.prevent="good.sl--" class="minus fl">-</a>
        </div>
      </li>
      <li class="col07">{{good.xj	}}</li>
      <li class="col08"><a href="" @click.prevent="delgood(good)">删除</a></li>
    </ul>
    <ul class="settlements">
      <li class="col01"><input type="checkbox" name="" v-model="checked" @click="select_all"></li>
      <li class="col02">全选</li>
      <li class="col03">合计(不含运费)：<span>¥</span><em>{{sum}}</em><br>共计<b>{{goods.length}}</b>件商品</li>
      <li class="col04"><a href="place_order">去结算</a></li>
    </ul>
    <div class="footer">
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
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Cart",
  mounted() {
    axios('http://localhost:8000/user/get_cart?user='+this.$store.state.user).then(res=>{
      this.goods = res.data;
      this.goods.forEach(item => {
        if (this.checkModel.indexOf(item.id) == -1) {
          this.checkModel.push(item.id)
        }
      });
    });
  },
  data(){
    return{
      goods: [],
      checked:true,
      checkModel:[]
    }
  },
  methods:{
    delgood(good){
      let index = this.goods.indexOf(good);
      this.goods.splice(index,1);
      axios('http://localhost:8000/user/delete_cart?id='+good.id).then(res=>{
        console.log(res.data);
      });
    },
    select_all(){
      if(this.checked == false) {
        this.goods.forEach(item => {
          if (this.checkModel.indexOf(item.id) == -1) {
            this.checkModel.push(item.id)
          }
        })
      }else{
        this.checkModel = [];
      }
    }
  },
  computed:{
    sum:function(){
      let sum = 0;
      for (let i of this.goods){
        sum += i.price*i.sl;
      }
      return sum.toFixed(1);
    },
  },
  watch:{
    goods:{
      handler(val, oldVal){
        for (let i of this.goods){
          i.xj = (i.price*i.sl).toFixed(1);
        }
      },
      deep:true
    },
    checkModel(){
      if(this.checkModel.length == this.goods.length){
        this.checked = true;
      }else{
        this.checked = false;
      }
    }
  }
}

</script>

<style scoped>

</style>