<script>
    import ProfRoomCard from "../components/ProfessorRoomCard.vue"
    import NavBar from "../components/NavBar.vue"
    import CornerStyle from "../components/CornerStyle.vue"
    import AddRoomButton from "../components/AddRoomButton.vue"

    import Header from "../components/Header.vue";
    import NavBtn from "../components/NavBtn.vue";
    export default {
        components: {
            ProfRoomCard, NavBar, Header, CornerStyle, NavBtn, AddRoomButton
        }
    }
</script>



<template>
    <div class="page-content">
        <Header title="Instructor Portal"/>
        <NavBtn/>

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
        { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/professor' },
        { title: 'Rooms', img: 'roomNav-icon.svg', route: '/professor/rooms' },
        { title: 'Inbox', img: 'mailNav-icon.svg', route: '/professor/inbox' },
        { title: 'Settings', img: 'settings-icon.svg', route: '/professor/settings' },
        { title: 'My Account', img: 'profile-icon.svg', route: '/professor/account' }]" />
        <div class="room-page-contents">
            <AddRoomButton buttonName="Make New Reservation"/>
            <div class = "room-cards">
                <ProfRoomCard cardColor='18ACFF' roomNum="101" bldg="Winston Chung" seatNum="30" approval="true" />
                <ProfRoomCard cardColor='18ACFF' roomNum="232" bldg="Bournes" seatNum="30" approval="false" />
            </div>
        </div>


        <CornerStyle />
    </div>
</template>