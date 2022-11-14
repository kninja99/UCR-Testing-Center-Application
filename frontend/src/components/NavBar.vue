<script>
    import NavElement from './NavElement.vue';
    export default {
        components: {
         NavElement
        }
    }
</script>

<template>
    <div class="nav-bar">
        <NavElement navTitle = "Dashboard" imgName = "dashBoard-icon.svg" route = "/admin"/>
        <NavElement navTitle = "Rooms" imgName = "roomNav-icon.svg" route = "admin/rooms"/>
        <NavElement navTitle = "Inbox" imgName = "mailNav-icon.svg" route = "admin/inbox"/>
        <NavElement navTitle = "Settings" imgName = "settings-icon.svg" route = "admin/settings"/>
        <NavElement navTitle = "My Account" imgName = "profile-icon.svg" route = "admin/account"/>
        <NavElement navTitle = "Logout" imgName = "logout-icon.svg" route = "/login"/>
    </div>
</template>