<template>
  <div class="popout">
    <div class="popout-content">
        <div class="popout-header">
            <h3>{{ popoutName }}</h3>
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