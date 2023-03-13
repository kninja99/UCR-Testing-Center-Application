<script>
export default {
  props: {
    title: String
  }
}
</script>

<template>
  <div class="popout">

    <div class="popout-content">
        <div class="popout-header">
          <p class="popout-title">{{ title }}</p>
          <button class="popout-close">x</button>
        </div>
        <slot></slot>
    </div>
  </div>
</template>
