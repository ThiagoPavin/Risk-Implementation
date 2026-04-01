using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class reader : MonoBehaviour
{
    public TextAsset World_textJSON;

    public TextAsset Turns_textJSON;

    public world_data world_Data = new world_data();

    public turns_data turns_data = new turns_data();

    private string world_json;

    private string Turns_json;


    void Awake()
    {

        world_Data = JsonUtility.FromJson<world_data>(World_textJSON.text);
        world_json = JsonUtility.ToJson(world_Data);

        turns_data = JsonUtility.FromJson<turns_data>(Turns_textJSON.text);
        Turns_json = JsonUtility.ToJson(turns_data);
    }
}

//myData = jsonUtility.FromJson<data>(textJSON.text)

//{"calls":[{"instanceID":0},{"instanceID":0},{"instanceID":0}]}
//{"calls":[{"instanceID":0},{"instanceID":0},{"instanceID":0}]}
//{"calls":[{"id":1,"tipo":"Move"},{"id":1,"tipo":"Attack"}]}