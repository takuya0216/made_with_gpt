<?php
    
 //秘密情報の定義
 define("SLACK_SIGNING_SECRET"  ,"79f87c86fc05f4e4b2a2883d68927532");
 define("SLACK_BOT_ACCESS_TOKEN","xoxb-4693566632567-4900607311424-xSjuQlsBV48fzc8HG4Gp50HZ");
    
 $base_input = file_get_contents("php://input");
    
 if(!verify_slack_request($base_input)){
   die('Recieved excepet slack request!');
 }
    
 $data = json_decode($base_input,true);
    
 if($data["type"] == "url_verification"){
   header('Content-Type: text/plain');
   echo $data["challenge"];
   die('Url verification complete');
 }
    
  if($data["type"] == "event_callback"){
   if(isset($data["event"]["bot_id"])){
    die('Bot message Ignored!');
   }
    
   // 自動応答メッセージの送信
   $message=$data["event"]["text"];
   send_slack_message($message,$data["event"]["channel"]);
 }
    
    
 // slackからの通信であることを確認するコード
 // 参照 https://api.slack.com/docs/verifying-requests-from-slack
 function verify_slack_request($base_input)
 {
   //必要なヘッダーがない場合はfalse
   if(!isset($_SERVER["HTTP_X_SLACK_REQUEST_TIMESTAMP"]) || !isset($_SERVER["HTTP_X_SLACK_SIGNATURE"])){
     return false;
   }
    
   //5分以上はfalse
   $request_timestamp = $_SERVER['HTTP_X_SLACK_REQUEST_TIMESTAMP'];
   if(abs(time() - $request_timestamp) > 60 * 5){
     return false;
   }
    
   $sig_basestring = "v0:" . $request_timestamp . ":" . $base_input;
   $my_signature = "v0=" . hash_hmac( "sha256", $sig_basestring, SLACK_SIGNING_SECRET);
   $slack_signature = $_SERVER["HTTP_X_SLACK_SIGNATURE"];
    
   // (PHP 5 >= 5.6.0, PHP 7) であればこっちを利用
   //return hash_equals($my_signature,$slack_signature);
   return ($my_signature === $slack_signature);
 }
    
    
 // 送信部分はfunctionにしてると便利
 function send_slack_message($message,$channel)
 {
     $ch = curl_init("https://slack.com/api/chat.postMessage"); 
     $data = http_build_query([
         "token" =>  SLACK_BOT_ACCESS_TOKEN,
         "channel" => $channel, 
         "text" => $message, 
         "username" => "bot",
     ]);
     curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
     curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
     curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
     $result = curl_exec($ch);
     curl_close($ch);
     return $result;
 }