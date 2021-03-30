function track_id(id){

    var checkBox = document.getElementById(id);
        if (checkBox.checked == true){
            // total_id.push(id)  // selected_ids came from selectAll click event
            selected_ids.push(id)
            let total_ids = document.getElementsByClassName("customSelect")
            if(total_ids.length == selected_ids.length)
            {
                $("#selectAll").prop('checked', true)
            }

        } else {
            if (selected_ids.includes(id)){
                // total_id.pop(id)
                $("#selectAll").prop('checked', false)
                let index = selected_ids.indexOf(id)
                selected_ids.splice(index, 1) // pop() removes only last element
            }
        }
        $('[name=selected_id]').val(selected_ids);
        if (selected_ids.length == 0) {
         $('#multi_status_change_panel').hide()
        }
        else{
            $('#multi_status_change_panel').show()     
        }
        console.log(selected_ids)
    }