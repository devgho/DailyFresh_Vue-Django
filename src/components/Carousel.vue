<template>
    <el-carousel trigger="click" height="270px">
      <el-carousel-item v-for="item in items" :key="item">
        <img :src="item.img" style="height: 100%;" alt="">
      </el-carousel-item>
    </el-carousel>
</template>

<script>
export default{
  name:'carousel',
  props: {
    items:{
      default:[
        {
          img:require('@/assets/images/slide.jpg')
        },
        {
          img:require('@/assets/images/slide02.jpg')
        },
        {
          img:require('@/assets/images/slide03.jpg')
        },
        {
          img:require('@/assets/images/slide04.jpg')
        },
      ]
    }
  },
  setup(props){
    return { props };
  }
}
</script>

<style scoped>
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
