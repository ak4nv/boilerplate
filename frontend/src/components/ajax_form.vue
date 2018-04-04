<template>
  <form :class="cls" @submit.prevent="$emit('submit', $event)" method="post">
    <fieldset :disabled="loading">
      <slot />
    </fieldset>
  </form>
</template>
<script>
  export default {
    props: {
      cls: {
        type: String,
        required: false,
        default: 'form'
      },
      loading: {
        type: Boolean,
        default: false
      }
    }
  }
</script>