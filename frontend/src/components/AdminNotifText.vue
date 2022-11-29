<script>
    import AdminNotifButtons from './AdminNotifButtons.vue';
    export default {
        components: {
            AdminNotifButtons
        },
        props: {
            profName: {
                type:String,
                required: true
            },
            className: {
                type:String,
                required: true
            },
            roomNum: {
                type:String,
                required: true
            }
        }
    }   
</script>

<template>
    <!-- 
            schedDateFrom: {
                type:Date,
                required: true
            },
            schedDateTo: {
                type:Date,
                required: true
            },
            schedTimeRange: {
                type:TimeRanges,
                required: true
            }

        <a :href="route" class= nav-comp>
        <img :src="require(`../assets/imgs/${imgName}`)" :alt="imgName">
        <h3>{{navTitle}}</h3>
    </a> -->
    <div class="admin-notif-text">
        <div class="prof-column">
            <p>Prof: {{profName}} <br>{{className}}</p>
        </div>

        <div class="room-column">
            <p>Room: {{roomNum}}</p>
        </div>
        
        <div class="sched-column">
            <p>Schedule</p>
        </div>
        <AdminNotifButtons />

    </div> 
</template>