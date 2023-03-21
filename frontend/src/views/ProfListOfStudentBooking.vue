<script>
    import Card from "../components/StudentRoomCard.vue"
    import NavBar from "../components/NavBar.vue"
    import CornerStyle from "../components/CornerStyle.vue"
    import Header from "../components/Header.vue";
    import NavBtn from "../components/NavBtn.vue";
    import BookedStudElem from "../components/ProfStudentListHasBookedElem.vue"
    import UnbookedStudElem from "../components/ProfStudentListNotBookedElem.vue"
    export default {
        components: {
            Card, NavBar, Header, CornerStyle, NavBtn, BookedStudElem, UnbookedStudElem
        }
    }
</script>

<template>
    <div class="page-content">
        <Header title="Students Booked"/>
        <NavBtn/>

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
        { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/professor' },
        { title: 'Rooms', img: 'roomNav-icon.svg', route: '/professor/rooms' },
        { title: 'Inbox', img: 'mailNav-icon.svg', route: '/professor/inbox' },
        { title: 'Settings', img: 'settings-icon.svg', route: '/professor/settings' },
        { title: 'My Account', img: 'profile-icon.svg', route: '/professor/account' }]" />
        <div class="student-test-sched-container">
            <BookedStudElem studentName='Kathleen Dario' className='CS178B'/>
            <BookedStudElem studentName='Kyle Damschen' className='CS178B'/>
            <UnbookedStudElem studentName='Gregory Griffith' className='CS178B'/>
            <UnbookedStudElem studentName='Eric Chu' className='CS178B'/>
        </div>
        <CornerStyle />
    </div>
</template>