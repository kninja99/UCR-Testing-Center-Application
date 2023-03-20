<script>
    import Card from "../components/StudentRoomCard.vue"
    import NavBar from "../components/NavBar.vue"
    import CornerStyle from "../components/CornerStyle.vue"
    import Header from "../components/Header.vue";
    import NavBtn from "../components/NavBtn.vue";
    import StudentTestElem from "../components/StudentTestSchedElement.vue"
    export default {
        
        data(){
            return {
                active: false
            };
        },
        // methods: {
            
        // },
        components: {
            Card, NavBar, Header, CornerStyle, NavBtn, StudentTestElem
        }
    }
</script>

<template>
    <div class="page-content">
        <Header title="Testing Rooms"/>
        <NavBtn/>

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
        { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/student' },
        { title: 'Rooms', img: 'roomNav-icon.svg', route: '/student/rooms' },
        { title: 'Inbox', img: 'mailNav-icon.svg', route: '/student/inbox' },
        { title: 'Settings', img: 'settings-icon.svg', route: '/student/settings' },
        { title: 'My Account', img: 'profile-icon.svg', route: '/student/account' }]" />
        <div class="student-test-sched-container">
            <StudentTestElem v-if="active=true" day='Tuesday' date='11/14/2023' bldgName='Winston Chung Hall' roomNum='223' timeBlock='10:00am - 11:00am' seatLeft='10'/>
            <StudentTestElem v-if="active=true" day='Wednesday' date='11/15/2023' bldgName='Dundee' roomNum='1003' timeBlock='1:00pm - 5:00pm' seatLeft='50'/>
        </div>
        <CornerStyle />
    </div>
</template>