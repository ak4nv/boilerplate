<template>
  <div>
    <notifications :store="store" />
    <template v-if="session.user">
      <top />
      <menu-block class="col-1" />
      <router-view class="col-11"></router-view>
    </template>
    <router-view v-else></router-view>
  </div>
</template>
<script>
  import top from './header.vue'
  import menuBlock from './menu.vue'
  import store from '../notifications/store.js'
  import notifications from '../notifications/component.vue'

  export default {
    components: { top, menuBlock, notifications },
    data () {
      return {
        session: Session,
        store: store
      }
    }
  }
</script>