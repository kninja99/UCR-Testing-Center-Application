<script>
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import NavBtn from "../components/NavBtn.vue";
import Header from "../components/Header.vue"
import CornerStyle from "../components/CornerStyle.vue"
import ProfApprovedNotif from "../components/ProfInboxApprovedElement.vue"
import ProfFlaggedNotif from "../components/ProfInboxFlaggedElement.vue"
import ProfDeniedNotif from "../components/ProfInboxDeclinedElement.vue"

export default {
    components: {
        Card, NavBar, NavBtn, Header, CornerStyle, ProfApprovedNotif, ProfFlaggedNotif, ProfDeniedNotif
    }
}
</script>

<template>
    <div class="page-content">
        <Header title="Instructor Inbox"/>
        <NavBtn/>
        <NavBar :nav-elements="[
            { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/professor' },
            { title: 'Rooms', img: 'roomNav-icon.svg', route: '/professor/rooms' },
            { title: 'Inbox', img: 'mailNav-icon.svg', route: '/professor/inbox' },
            { title: 'Settings', img: 'settings-icon.svg', route: '/professor/settings' },
            { title: 'My Account', img: 'profile-icon.svg', route: '/professor/account' }]" />
        <div class="admin-notif-container"> <!-- using same styling -->
            <ProfApprovedNotif adminName='Allan Knight' className='CS061' roomNum='234' schedDate="2/16/2024" schedTimeFrom="10:00AM" schedTimeTo="4:00PM"/>
            <ProfDeniedNotif adminName='Admin Person something' className='CS167' roomNum='405' schedDate="6/1/2025" schedTimeFrom="8:00AM" schedTimeTo="6:00PM"/>
            <ProfFlaggedNotif studentName='Kathleen Dario' className='CS178B' roomNum='341' schedDate="11/16/2023" schedTimeFrom="9:00AM" schedTimeTo="10:00AM"/>
        </div>
        <CornerStyle />
    </div>
</template>