<template>
  <div class="popout">
    <div class="popout-content">
        <div class="popout-header">
            <p class="popout-name">{{ popoutName }}</p>
            <button class="close-popout">X</button>
        </div>
        <slot></slot>
    </div>
  </div>
</template>

<script>

export default {
    props: {
        popoutName: String
    }
}

</script>