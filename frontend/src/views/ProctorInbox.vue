<script>
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import NavBtn from "../components/NavBtn.vue";
import Header from "../components/Header.vue"
import CornerStyle from "../components/CornerStyle.vue"
import ProcInboxElem from "../components/ProctorInboxElement.vue"

export default {
    components: {
        Card, NavBar, NavBtn, Header, CornerStyle, ProcInboxElem
    }
}
</script>

<template>
    <div class="page-content">
        <Header title="Proctor Inbox"/>
        <NavBtn/>
        <NavBar :nav-elements="[
            { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/proctor' },
            { title: 'Rooms', img: 'roomNav-icon.svg', route: '/proctor/rooms' },
            { title: 'Inbox', img: 'mailNav-icon.svg', route: '/proctor/inbox' },
            { title: 'Settings', img: 'settings-icon.svg', route: '/proctor/settings' },
            { title: 'My Account', img: 'profile-icon.svg', route: '/proctor/account' }]" />
        <div class="student-checkin-container">
            <ProcInboxElem senderName='Prof Knight' subject='CS152 Test' message='CS 152 test at 2pm is open notes' receivedDate='03/19/2023' receivedTime='@10:32AM' />
            <ProcInboxElem senderName='Prof Knight' subject='CS152 Test' message='CS 152 test at 2pm is open notes and open book' receivedDate='03/19/2023' receivedTime='@10:32AM' />
        </div>
        <CornerStyle />
    </div>
</template>