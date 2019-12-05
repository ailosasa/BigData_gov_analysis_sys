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
      event_deals: {
        '处置中': {
          'proportion': 40,
          'events':
            {
              '市容环卫': 20,
              '环保水务': 30,
              '市政设施': 20,
              '……': 30
            }
        },
        '超期办结': {
          'proportion': 30,
          'events':
            {
              '市容环卫': 20,
              '环保水务': 30,
              '市政设施': 20,
              '……': 30
            }
        },
        '按期办结': {
          'proportion': 30,
          'events':
            {
              '市容环卫': 20,
              '环保水务': 30,
              '市政设施': 20,
              '……': 30
            }
        }
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
      var option = this.add_date_event()// 准备图表数据
      
      myChart.setOption(option)
    },
    add_date_event () {
      var option = {
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b}: {c} ({d}%)'
        },
        legend: {
          orient: 'vertical',
          x: 'left',
          data: [] // 获取全部的图例
        },
        series: [
          {
            name: '办结情况',
            type: 'pie',
            selectedMode: 'single',
            radius: [0, '30%'],

            label: {
              normal: {
                position: 'inner'
              }
            },
            labelLine: {
              normal: {
                show: false
              }
            },
            data: [] // 获取具体办结情况数据
          },
          {
            name: '访问来源',
            type: 'pie',
            radius: ['40%', '55%'],
            label: {
              normal: {
                formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                backgroundColor: '#eee',
                borderColor: '#aaa',
                borderWidth: 1,
                borderRadius: 4,
                // shadowBlur:3,
                // shadowOffsetX: 2,
                // shadowOffsetY: 2,
                // shadowColor: '#999',
                // padding: [0, 7],
                rich: {
                  a: {
                    color: '#999',
                    lineHeight: 22,
                    align: 'center'
                  },
                  // abg: {
                  //     backgroundColor: '#333',
                  //     width: '100%',
                  //     align: 'right',
                  //     height: 22,
                  //     borderRadius: [4, 4, 0, 0]
                  // },
                  hr: {
                    borderColor: '#aaa',
                    width: '100%',
                    borderWidth: 0.5,
                    height: 0
                  },
                  b: {
                    fontSize: 16,
                    lineHeight: 33
                  },
                  per: {
                    color: '#eee',
                    backgroundColor: '#334455',
                    padding: [2, 4],
                    borderRadius: 2
                  }
                }
              }
            },
            data: [] // 获取外层办结情况下事件类型分类的数据
          }
        ]
      }// 准备图表数据
      for (var name in this.event_deals) {
        option.legend.data.push(name)
        for (var l_name in this.event_deals[name].events) {
          option.legend.data.push(l_name)
        }
      }
      for (var deal in this.event_deals) { // 准备series[1]的数据
        var data = {
          value: this.event_deals[deal].proportion,
          name: deal
        }
        option.series[0].data.push(data)
      }
      for (deal in this.event_deals) {
        data = []
        for (var event in this.event_deals[deal].events) {
          data.push({value: this.event_deals[deal].events[event], name: event})
        }
        
        if (deal === '处置中') { option.series[1].data = data }
      }
      
      return option
    }
  }
}
</script>
