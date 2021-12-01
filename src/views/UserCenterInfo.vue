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
      <div class="sub_page_name fl">|&nbsp;&nbsp;&nbsp;&nbsp;用户中心</div>
    </div>

    <div class="main_con clearfix">
      <div class="left_menu_con clearfix">
        <h3>用户中心</h3>
        <ul>
          <li><a href="#" :class="{active:now=='user_info'}" @click.prevent="now='user_info'">· 个人信息</a></li>
          <li><a href="#" :class="{active:now=='address'}" @click.prevent="now='address'">· 收货地址</a></li>
        </ul>
      </div>
      <div v-if="now == 'user_info'">
        <div class="right_content clearfix">
          <div class="info_con clearfix">
            <h3 class="common_title2">基本信息</h3>
            <ul class="user_info_list">
              <li><span>用户名：</span>{{user_info.username}}</li>
              <li><span>注册时间：</span>{{user_info.add_time}}</li>
              <li><span>手机号码：</span>{{user_info.phone}}</li>
              <li><span>邮编：</span>{{user_info.post_code}}</li>
            </ul>
          </div>
        </div>
      </div>
      <div v-if="now == 'user_order'">
        <div class="right_content clearfix">
          <h3 class="common_title2">全部订单</h3>
          <div v-for="order in user_order">
            <ul class="order_list_th w978 clearfix">
              <li class="col01">{{order.time}}</li>
              <li class="col02">{{order.SN}}</li>
              <li class="col02 stress">{{order.status}}</li>
            </ul>

            <table class="order_list_table w980">
              <tbody>
              <tr>
                <td width="55%">
                  <ul class="order_goods_list clearfix" v-for="good in order.goods">
                    <li class="col01"><img :src="good.img"></li>
                    <li class="col02">{{good.name}}<em>{{good.weight}}g</em></li>
                    <li class="col03">{{good.num}}</li>
                    <li class="col04">{{good.price}}元</li>
                  </ul>
                </td>
                <td width="15%">{{order.price}}元</td>
                <td width="15%">{{order.status}}</td>
                <td width="15%" v-if="order.status=='未支付'"><a href="#" class="oper_btn">去付款</a></td>
                <td width="15%" v-if="order.status=='已支付'"><a href="#" class="oper_btn" >查物流</a></td>
              </tr>
              </tbody>
            </table>
          </div>

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
      <div v-if="now == 'address'">
        <div class="right_content clearfix">
          <h3 class="common_title2">收货地址</h3>
          <div class="site_con">
            <dl>
              <dt>当前地址：</dt>
              <dd>{{address}}</dd>
            </dl>
          </div>
          <h3 class="common_title2">编辑地址</h3>
          <div class="site_con">
            <form>
              <div class="form_group">
                <label>收件人：</label>
                <input type="text" name="" v-model="user_info.receiver">
              </div>
              <div class="form_group">
                <label>详细地址：</label>
                <input type="text" name="" v-model="user_info.address">
              </div>
              <div class="form_group">
                <label>邮编：</label>
                <input type="text" name="" v-model="user_info.post_code">
              </div>
              <div class="form_group">
                <label>手机：</label>
                <input type="text" name="" v-model="user_info.phone">
              </div>

              <input type="submit" name="" value="提交" class="info_submit" @click.prevent="commit">
            </form>
          </div>
        </div>
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
    <p>CopyRight © 2016 北京天天生鲜信息技术有限公司 All Rights Reserved</p>
    <p>电话：010-****888 京ICP备*******8号</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "UserCenterInfo",
  data(){
    return {
      now: "user_info",
      user_info: {
        username: '18210569700',
        contact: '18210569700',
        address: '北京市昌平区',
        recent: [
          { name: '草莓', img: 'images/goods/goods003.jpg', price: '30.00', weight: '500g' },
          { name: '柠檬', img: 'images/goods/goods001.jpg', price: '16.80', weight: '500g' },
          { name: '虾仁', img: 'images/goods/goods018.jpg', price: '100.00', weight: '500g' },
          { name: '樱桃', img: 'images/goods/goods017.jpg', price: '32.00', weight: '500g' },
        ]
      },
      user_order: [{
        time: '2016-8-21 17:36:24',
        order_SN: '56872934',
        status: '未支付',
        goods: [
          { name: '苹果', img: 'images/goods02.jpg', price: '11.80', weight: '500g', num: 1 },
          { name: '苹果', img: 'images/goods02.jpg', price: '11.80', weight: '500g', num: 1 }
        ],
        price: '33.60',
      }, {
        time: '2016-8-21 17:36:24',
        order_SN: '56872934',
        status: '已支付',
        goods: [
          { name: '苹果', img: 'images/goods02.jpg', price: '11.80', weight: '500g', num: 1 },
          { name: '苹果', img: 'images/goods02.jpg', price: '11.80', weight: '500g', num: 1 }
        ],
        price: '33.60',
      },],
      address:'北京市 海淀区 东北旺西路8号中关村软件园 （李思 收） 182****7528'
    }
  },
  mounted() {
    axios('http://localhost:8000/user/get_user/?user='+this.$store.state.user).then(res=>{
      this.user_info = res.data[0];
      this.address=this.user_info.address+`(${this.user_info.receiver} 收) ${this.user_info.phone}`;
    });
  },
  methods:{
    commit(){
      axios(`http://localhost:8000/user/change/?user=${this.$store.state.user}&address=${this.user_info.address}&receiver=${this.user_info.receiver}&phone=${this.user_info.phone}&post_code=${this.user_info.post_code}`).then(res=>{
        console.log(res.data);
        axios('http://localhost:8000/user/get_user/?user='+this.$store.state.user).then(res=>{
          this.user_info = res.data[0];
          this.address=this.user_info.address+`(${this.user_info.receiver} 收) ${this.user_info.phone}`;
        });
      });
    }
  }
}
</script>

<style scoped>

</style>