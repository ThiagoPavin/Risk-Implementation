using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

[System.Serializable]
public class country
{
    public string name;
    public int owner;
    public int n_troops;

    public int owner_first;
    public int n_troops_first;

    public int owner_first_command;
    public int n_troops_first_command;
    
    public TextMeshProUGUI text;
    public SpriteRenderer sprite;
}