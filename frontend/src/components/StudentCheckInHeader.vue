<script>
export default {
    props: {
        status: String,
        imgName: String,
        route: String
    }
}   
</script>

<template>
    <div class="status-header">
        <router-link :to="route">
            <button class="status">{{ status }}</button>
        </router-link>
        <h1 class="status">Status</h1>
        <h2 class="name">Name</h2>
        <h3 class="class">Class</h3>
        <h4 class="professor">Professor</h4>
        <h5 class="actions">Actions</h5>
    </div>
</template>