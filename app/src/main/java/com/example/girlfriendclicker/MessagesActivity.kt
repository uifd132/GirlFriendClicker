package com.example.girlfriendclicker

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.WindowManager
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.widget.AppCompatImageButton

class MessagesActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        window.setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN)
        setContentView(R.layout.activity_messages)

        val affectionTextView: TextView = findViewById(R.id.affectionTextView)
        val messageClickButton: Button = findViewById(R.id.messageClickButton)

        var affection: Int = 0


        messageClickButton.setOnClickListener {
            affection += 1
            affectionTextView.text = (affection.toString())
        }
    }
}