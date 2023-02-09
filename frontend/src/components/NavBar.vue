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
    },
    methods: {
        logoutEvent() {
            this.$store.commit('logout');
            console.log(this.$store.state);
        }
    }
}
</script>

<template>
    <div class="nav-bar">
        <!-- loops over our navElements and creates those nav elements -->
        <NavElement v-for="(item) in navElements" :nav-title="item.title" :img-name="item.img" :route="item.route" />
        <NavElement @click="logoutEvent" nav-title="logout" img-name="logout-icon.svg" route="/login" />
    </div>
</template>