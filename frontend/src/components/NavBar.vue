<script>
    import NavElement from './NavElement.vue';
    export default {
        components: {
         NavElement
        },
        props: {
            // structure of array
            // [{title: String , img:String , route: String}, ...]
            navElements: {
                type: Array,
                required: true
            }
        }
    }
</script>

<template>
    <div class="nav-bar">
        <!-- loops over our navElements and creates those nav elements -->
        <NavElement v-for="(item) in navElements" :nav-title = "item.title" :img-name = "item.img" :route = "item.route"/>
    </div>
</template>