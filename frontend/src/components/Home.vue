<template>
    <div class="home">
        <div class="container mt-4 pt-4">
            <h1>Welcome</h1>
            <img src="http://f.code-on.be/d/18/04/2415pnF0.png" class="img-fluid">

            <div class="row">
                <div class="col-md-3">
                    <router-link to="/apps/" class="nav-link" active-class="active">Create apps and models</router-link>
                </div>
                <div class="col-md-2">
                    <router-link to="/settings/" class="nav-link" active-class="active">Change settings</router-link>
                </div>
                <div class="col-md-2">
                    <router-link to="/plugins/" class="nav-link" active-class="active">Install some plugins</router-link>
                </div>
            </div>
        </div>

    </div>
</template>

<script>

export default {
    name: 'home',

}
</script>
