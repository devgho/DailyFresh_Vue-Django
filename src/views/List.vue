<template>
  <div id="wzw">
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
      <div class="search_con fl">
        <input type="text" class="input_text fl" name="" placeholder="搜索商品" @keyup.enter="search" v-model="keyword">
        <input type="button" class="input_btn fr" name="" value="搜索" @click="search">
      </div>
      <div class="guest_cart fr">
        <a href="cart" class="cart_name fl">我的购物车</a>
      </div>
    </div>

    <div class="main_wrap clearfix">
      <div class="l_wrap fl clearfix">
        <div class="new_goods">
          <h3>新品推荐</h3>
          <ul>
            <li v-for="good in news">
              <a :href="sendURL(good.id)"><img :src="good.img"></a>
              <h4><a href="#">{{good.name}}</a></h4>
              <div class="prize">￥{{good.price}}</div>
            </li>
          </ul>
        </div>
      </div>

      <div class="r_wrap fr clearfix">
        <div class="sort_bar">
          <!-- <a href="#" class="active">新鲜水果</a> -->
          <a href="#" v-for="type in types" @click.prevent="act(type, $event)">{{type.name}}</a>
        </div>

        <ul class="goods_type_list clearfix">
          <div v-for="good in goods">
            <li v-if="good.category_id == type || type==''">
              <a :href="sendURL(good.id)"><img :src="good.img"></a>
              <h4><a href="detail">{{good.name}}</a></h4>
              <div class="operate">
                <span class="prize">￥{{good.price}}</span>
                <span class="unit">{{good.weight}}</span>
              </div>
            </li>
          </div>
        </ul>

        <div class="pagenation">
          <a href="#">上一页</a>
          <a href="#" class="active">1</a>
          <a href="#">2</a>
          <a href="#">3</a>
          <a href="#">4</a>
          <a href="#">5</a>
          <a href="#">下一页></a>
        </div>
      </div>
    </div>

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
      <p>电话：010-****888 京ICP备*******8号</p>
    </div>
  </div>
</template>

<script>
import {get_goods} from "@/network/request";
import axios from "axios";

export default {
  name: "List",
  methods:{
    act(type,that){
      this.old_e.className = "";
      this.old_e = that.currentTarget;
      that.currentTarget.className="active";
      this.type = type.id;
    },
    search(){
      get_goods('limit=40&name='+this.keyword).then(res=>{
        this.goods = res.data;
        console.log(this.goods[0]);
      }).catch(err=>{
        console.log(err);
      })
    },
    sendURL(id){
      return 'detail?id='+id;
    }
  },
  mounted(){
    this.keyword = this.$route.query.name;
    axios.get('http://localhost:8000/goods/get_types').then(res=>{
      this.types = res.data;
    });
    let item = ['水果','海鲜', '肉类','蛋品','蔬菜','速冻'];
    let randItem = item[Math.floor((Math.random() * item.length))];
    axios.get('http://localhost:8000/goods/get_goods?limit=2&category='+randItem).then(res=>{
      this.news = res.data;
    });
    axios.get('http://localhost:8000/goods/get_goods?limit=40').then(res=>{
      this.goods = res.data;
    });
    if (this.keyword != '' && this.keyword != undefined){
      this.search();
    }
  },
  data(){
    return{
      old_e:{},
      type:'',
      types:['水果','海鲜', '肉类','蛋品','蔬菜','速冻'],
      goods:[],
      news:[],
      keyword:''
    }
  }
}
</script>

<style scoped>

</style>