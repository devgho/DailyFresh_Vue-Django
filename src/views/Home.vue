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
      <div class="guest_cart fr" v-if="this.$store.state.user!=''">
        <a href="cart" class="cart_name fl">我的购物车</a>
      </div>
    </div>

    <div class="navbar_con">
      <div class="navbar">
        <h1 class="fl">全部商品分类</h1>
      </div>
    </div>

    <div class="center_con clearfix">
      <ul class="subnav fl">
        <li><a href="#model01" class="fruit">新鲜水果</a></li>
        <li><a href="#model02" class="seafood">海鲜水产</a></li>
        <li><a href="#model03" class="meet">猪牛羊肉</a></li>
        <li><a href="#model04" class="egg">禽类蛋品</a></li>
        <li><a href="#model05" class="vegetables">新鲜蔬菜</a></li>
        <li><a href="#model06" class="ice">速冻食品</a></li>
      </ul>
      <div class="slide fl">
        <Carousel></Carousel>
      </div>
      <div class="adv fl">
        <a href="#"><img src="@/assets/images/adv01.jpg"></a>
        <a href="#"><img src="@/assets/images/adv02.jpg"></a>
      </div>
    </div>

    <!-- 新鲜水果start -->
    <div class="list_model">
      <div class="list_title clearfix">
        <h3 class="fl" id="model01">新鲜水果</h3>
        <a href="list" class="goods_more fr" id="fruit_more">查看更多 ></a>
      </div>

      <div class="goods_con clearfix">
        <div class="goods_banner fl"><img src="@/assets/images/banner01.jpg"></div>
        <ul class="goods_list fl">
          <li v-for="f in fruit">
            <h4><a :href="sendURL(f.id)">{{f.name}}</a></h4>
            <a :href="sendURL(f.id)"><img :src="f.img"></a>
            <div class="prize">¥ {{f.price}}</div>
          </li>
        </ul>
      </div>
    </div>
    <!-- 新鲜水果end -->

    <div class="list_model">
      <div class="list_title clearfix">
        <h3 class="fl" id="model02">海鲜水产</h3>
        <a href="list" class="goods_more fr">查看更多 ></a>
      </div>

      <div class="goods_con clearfix">
        <div class="goods_banner fl"><img src="@/assets/images/banner02.jpg"></div>
        <ul class="goods_list fl">
          <li v-for="sea in seafood">
            <h4><a :href="sendURL(sea.id)">{{sea.name}}</a></h4>
            <a :href="sendURL(sea.id)"><img :src="sea.img"></a>
            <div class="prize">¥ {{sea.price}}</div>
          </li>
        </ul>
      </div>
    </div>
    <div class="list_model">
      <div class="list_title clearfix">
        <h3 class="fl" id="model03">猪牛羊肉</h3>
        <a href="list" class="goods_more fr">查看更多 ></a>
      </div>

      <div class="goods_con clearfix">
        <div class="goods_banner fl"><img :src='require("@/assets/images/banner03.jpg")'></div>
        <ul class="goods_list fl">
          <li v-for="m in meat">
            <h4><a :href="sendURL(m.id)">{{m.name}}</a></h4>
            <a :href="sendURL(m.id)"><img :src="m.img"></a>
            <div class="prize">¥ {{m.price}}</div>
          </li>
        </ul>
      </div>
    </div>
    <div class="list_model">
      <div class="list_title clearfix">
        <h3 class="fl" id="model04">禽类蛋品</h3>
        <a href="list" class="goods_more fr">查看更多 ></a>
      </div>

      <div class="goods_con clearfix">
        <div class="goods_banner fl"><img src="@/assets/images/banner04.jpg"></div>
        <ul class="goods_list fl">
          <li v-for="e in egg">
            <h4><a :href="sendURL(e.id)">{{e.name}}</a></h4>
            <a :href="sendURL(e.id)"><img :src="e.img"></a>
            <div class="prize">¥ {{e.price}}</div>
          </li>
        </ul>
      </div>
    </div>
    <div class="list_model">
      <div class="list_title clearfix">
        <h3 class="fl" id="model05">新鲜蔬菜</h3>
        <a href="list" class="goods_more fr">查看更多 ></a>
      </div>

      <div class="goods_con clearfix">
        <div class="goods_banner fl"><img src="@/assets/images/banner05.jpg"></div>
        <ul class="goods_list fl">
          <li v-for="v in vegetable">
            <h4><a :href="sendURL(v.id)">{{v.name}}</a></h4>
            <a :href="sendURL(v.id)"><img :src="v.img"></a>
            <div class="prize">¥ {{v.price}}</div>
          </li>
        </ul>
      </div>
    </div>
    <div class="list_model">
      <div class="list_title clearfix">
        <h3 class="fl" id="model06">速冻食品</h3>
        <a href="list" class="goods_more fr">查看更多 ></a>
      </div>

      <div class="goods_con clearfix">
        <div class="goods_banner fl"><img src="@/assets/images/banner06.jpg"></div>
        <ul class="goods_list fl">
          <li v-for="i in ice">
            <h4><a :href="sendURL(i.id)">{{i.name}}</a></h4>
            <a :href="sendURL(i.id)"><img :src="i.img"></a>
            <div class="prize">¥ {{i.price}}</div>
          </li>
        </ul>
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
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import {onMounted, reactive, ref} from "vue";
import Carousel from '../components/Carousel';
import axios from 'axios';
import router from "@/router";
import {useStore} from "vuex";

export default {
  name: 'Home',
  components: {
    HelloWorld,
    Carousel
  },
  setup(){
    const store = useStore();
    const fruit = ref();
    const seafood = ref();
    const meat = ref();
    const egg = ref();
    const vegetable = ref();
    const ice = ref();
    let user = store.state.user;
    function sendURL(id){
      return 'detail?id='+id;
    };
    onMounted(()=>{
      axios.get('http://localhost:8000/goods/get_goods?limit=4&category=水果').then(res=>{
        fruit.value = res.data;
      });
      axios.get('http://localhost:8000/goods/get_goods?limit=4&category=海鲜').then(res=>{
        seafood.value = res.data;
      });
      axios.get('http://localhost:8000/goods/get_goods?limit=4&category=蛋品').then(res=>{
        egg.value = res.data;
      });
      axios.get('http://localhost:8000/goods/get_goods?limit=4&category=肉类').then(res=>{
        meat.value = res.data;
      });
      axios.get('http://localhost:8000/goods/get_goods?limit=4&category=蔬菜').then(res=>{
        vegetable.value = res.data;
      });
      axios.get('http://localhost:8000/goods/get_goods?limit=4&category=速冻').then(res=>{
        ice.value = res.data;
      });
    });
    let keyword = ref();
    function search(){
      router.push({name:'List',query:{name:this.keyword}});
    }
    return {
      sendURL,
      fruit,
      seafood,
      meat,
      egg,
      ice,
      vegetable,
      keyword,
      search,
      user
    };
  }
}
</script>

<style scoped>
  @import '~@/assets/css/main.css';
  @import '~@/assets/css/reset.css';
</style>