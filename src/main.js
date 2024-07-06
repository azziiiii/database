import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import 'font-awesome/css/font-awesome.min.css';
import request from '@/utils/request';

Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.prototype.$request = request

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
