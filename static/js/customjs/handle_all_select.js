function handleAllSelect(){
        selected_ids = [];
        let all_elements = document.getElementsByClassName('customSelect');
        let all_ids = []
        let one_unchecked = false

        for(let i=0; all_elements[i]; ++i){
            if(!all_elements[i].checked){
                one_unchecked = true; // check whether at least one box is unselected or not
            }
            all_ids.push(all_elements[i].getAttribute('id'))
        }

        if(one_unchecked){
            $(".customSelect").prop("checked", true);
            $('[name=selected_id]').val(selected_ids);
            selected_ids = all_ids;
        }else{
            $(".customSelect").prop("checked", false);
            $("#selectAll").prop('checked', false);
            selected_ids = []
        }

        $("input[name='selected_id']").val(selected_ids);
}