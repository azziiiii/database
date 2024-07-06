<template>
  <router-view></router-view>
</template>

<script>
import Login from "./pages/Login.vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    Login,
  },
  data() {
    return {};
  },
  methods: {},
};
</script>
