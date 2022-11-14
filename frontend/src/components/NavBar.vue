<script>
    import NavElement from './NavElement.vue';
    export default {
        components: {
         NavElement
        },
        props: {
            navElements: Array
        }
    }
</script>

<!-- <template>
    <div class="nav-bar">
        <NavElement nav-title = "Dashboard" img-name = "dashBoard-icon.svg" route = "/admin"/>
        <NavElement nav-title = "Rooms" img-name = "roomNav-icon.svg" route = "admin/rooms"/>
        <NavElement nav-title = "Inbox" img-name = "mailNav-icon.svg" route = "admin/inbox"/>
        <NavElement nav-title = "Settings" img-name = "settings-icon.svg" route = "admin/settings"/>
        <NavElement nav-title = "My Account" img-name = "profile-icon.svg" route = "admin/account"/>
        <NavElement nav-title = "Logout" img-name = "logout-icon.svg" route = "/login"/>
    </div>
</template> -->

<template>
    <div class="nav-bar">
        <NavElement nav-title = "Dashboard" img-name = "dashBoard-icon.svg" route = "/admin"/>
        <NavElement nav-title = "Rooms" img-name = "roomNav-icon.svg" route = "admin/rooms"/>
        <NavElement nav-title = "Inbox" img-name = "mailNav-icon.svg" route = "admin/inbox"/>
        <NavElement nav-title = "Settings" img-name = "settings-icon.svg" route = "admin/settings"/>
        <NavElement nav-title = "My Account" img-name = "profile-icon.svg" route = "admin/account"/>
        <NavElement nav-title = "Logout" img-name = "logout-icon.svg" route = "/login"/>
    </div>
</template>