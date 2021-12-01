<template>
  <div id="feng">
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


    <div class="goods_detail_con clearfix">
      <div class="goods_detail_pic fl"><img :src="good.img" style="width: 300px;height: 300px;"></div>

      <div class="goods_detail_list fr">
        <h3>{{good.name}}</h3>
        <p>{{good.profile}}</p>
        <div class="prize_bar">
          <span class="show_pirze">¥<em>{{good.price}}</em></span>
          <span class="show_unit">单 位：500g </span>
        </div>
        <div class="goods_num clearfix">
          <div class="num_name fl">数 量：</div>
          <div class="num_add fl">
            <input type="text" class="num_show fl" v-model="nums">
            <a href="javascript:;" class="add fr" @click="nums++">+</a>
            <a href="javascript:;" class="minus fr" @click="nums--">-</a>
          </div>
        </div>
        <div class="total">总价：<em>{{good.price}}元</em></div>
        <div class="operate_btn">
          <a href="javascript:;" class="buy_btn">立即购买</a>
          <a href="javascript:;" class="add_cart" id="add_cart" @click="add_cart(good.id)">加入购物车</a>
        </div>
      </div>
    </div>

    <div class="main_wrap clearfix">
      <div class="l_wrap fl clearfix">
        <div class="new_goods">
          <h3>新品推荐</h3>
          <ul>
            <li v-for="good in news">
              <a :href="sendURL(good.id)"><img :src="good.img"></a>
              <h4><a :href="sendURL(good.id)">{{good.name}}</a></h4>
              <div class="prize">￥{{good.price}}</div>
            </li>
          </ul>
        </div>
      </div>

      <div class="r_wrap fr clearfix">
        <ul class="detail_tab clearfix">
          <li class="active">商品介绍</li>
        </ul>

        <div class="tab_content" >
          <dl>
            <dt>商品详情：</dt>
            <dd>{{good.brief}}</dd>
          </dl>
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
      <p>电话：010-****888    京ICP备*******8号</p>
    </div>
    <div class="add_jump"></div>
  </div>
</template>

<script>
import axios from "axios";
import router from "@/router";

export default {
  name: "Detail",
  data(){
    return {
      news:[],
      good:{},
      nums:1,
      keyword:''
    }
  },
  methods:{
    sendURL(id){
      return '?id='+id;
    },
    add_cart(good_id){
      axios(`http://localhost:8000/user/post_cart/?user_id=${this.$store.state.user}&good_id=${good_id}&nums=${this.nums}`).then(res=>{
        alert('添加成功');
      });
    },
    search(){
      router.push({name:'List',query:{name:this.keyword}});
    }
  }
  ,
  mounted(){
    let search = window.location.search;
    axios.get('http://localhost:8000/goods/get_goods?id='+search.split("=")[1]).then(res=>{
      this.good = res.data[0];
      console.log(this.good);
    });
    let items = ['水果','海鲜','肉类','蛋类','蔬菜','速冻'];
    let randomItem = items[Math.floor(Math.random() * items.length)];
    axios.get('http://localhost:8000/goods/get_goods?limit=2&category='+randomItem).then(res=>{
      this.news = res.data;
    });

  }
}
</script>

<style scoped>

</style>