<template>
  <div class="content">
    <div class="container-fluid">
      <div id="myChart" :style="{width: '600px', height: '300px'}"></div>
    </div>
  </div>
</template>

<script>

export default {
  data () {
    return {
      todayLivelihood: {
        'appretiate': 36,
        'complaint': 7,
        'advice': 57
      }
    }
  },
  mounted () {
    this.drawLine()
  },
  methods: {
    drawLine () {
      // 基于准备好的dom，初始化echarts实例
      let myChart = this.$echarts.init(document.getElementById('myChart'))
      // 绘制图表
      var PieData = []
      this.add_date_pie(PieData)
      
      var setting = [
        {
          name: '访问来源',
          type: 'pie',
          radius: '55%',
          data: PieData
        }
      ]
      myChart.setOption({
        series: setting
      })
    },
    add_date_pie (PieData) {
      var item
      var dvalue
      var dname
      for (item in this.todayLivelihood) {
        dvalue = this.todayLivelihood[item]
        dname = item
        var ADate = {}
        ADate['name'] = dname
        ADate['value'] = dvalue
        
        PieData.push(ADate)
        
      }
    }
  }
}
</script>
